<template>
  <div>
    <Navbar/>
    <div id="login-modal" role="dialog">
      <div class="loginmodal-container">
        <h1>Logowanie</h1>
        <br>
        <form @submit.prevent="login">
          <div class="form-group">
            <input
              type="text"
              v-model="username"
              name="username"
              placeholder="Nazwa użytkownika"
              class="form-control"
              :class="{ 'is-invalid': submitted && !username }"
            >
            <input
              type="password"
              v-model="password"
              name="password"
              placeholder="Hasło"
              class="form-control"
              :class="{ 'is-invalid': submitted && !password }"
            >
            <div v-show="submitted && !password" class="invalid-feedback">Hasło jest wymagane!</div>
            <input type="submit" name="login" class="login loginmodal-submit" v-model="loginBtnTxt">
          </div>
        </form>

        <div class="login-help">
          <router-link to="/zarejestruj">Zarejestruj się</router-link>-
          <a href="#">Zapomniałeś hasła?</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

export default {
  data() {
    return {
      loginBtnTxt: "Zaloguj się",
      username: "",
      password: "",
      submitted: false,
      previousPath: ""
    };
  },
  methods: {
    login: function() {
      this.submitted = true;

      axios
        .post("http://185.238.73.103:8008/api/api-auth/?format=json", {
          username: this.username,
          password: this.password
        })
        .then(response => {
          localStorage.setItem("token", response["data"]["token"]);

          axios
            .get(
              "http://185.238.73.103:8008/api/profiles/user_details?username=" +
                this.username,
              {
                headers: {
                  Authorization: "Token " + localStorage.getItem("token")
                }
              }
            )
            .then(response => {
              localStorage.setItem("profile", JSON.stringify(response["data"]));
              this.loginBtnTxt = "Zalogowano!";

              if (this.previousPath === "/stworz-oferte") {
                this.$router.back();
              } else {
                this.$router.push();
              }
            })
            .catch(error => {
              console.log(error);
              this.loginBtnTxt = "Nieznany błąd!";
            });
        })
        .catch(error => {
          if (error.response.status == 400) {
            this.loginBtnTxt = "Złe dane!";
          } else {
            this.loginBtnTxt = "Nieznany błąd!";
          }
        });
    }
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.previousPath = from.path;
    });
  },
  components: {
    Navbar
  }
};
</script>

<style scoped>
@import url(http://fonts.googleapis.com/css?family=Roboto);

#login-modal {
  margin-top: 50px;
}

.loginmodal-container {
  padding: 30px;
  max-width: 350px;
  width: 100% !important;
  background-color: #f7f7f7;
  margin: 0 auto;
  border-radius: 2px;
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  font-family: roboto;
}

.loginmodal-container h1 {
  text-align: center;
  font-size: 1.8em;
  font-family: roboto;
}

.loginmodal-container input[type="submit"] {
  width: 100%;
  display: block;
  margin-bottom: 10px;
  position: relative;
}

.loginmodal-container input[type="text"],
input[type="password"] {
  height: 44px;
  font-size: 16px;
  width: 100%;
  margin-bottom: 10px;
  -webkit-appearance: none;
  background: #fff;
  border: 1px solid #d9d9d9;
  border-top: 1px solid #c0c0c0;
  /* border-radius: 2px; */
  padding: 0 8px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
}

.loginmodal-container input[type="text"]:hover,
input[type="password"]:hover {
  border: 1px solid #b9b9b9;
  border-top: 1px solid #a0a0a0;
  -moz-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}

.loginmodal {
  text-align: center;
  font-size: 14px;
  font-family: "Arial", sans-serif;
  font-weight: 700;
  height: 36px;
  padding: 0 8px;
  /* border-radius: 3px; */
  /* -webkit-user-select: none;
  user-select: none; */
}

.loginmodal-submit {
  /* border: 1px solid #3079ed; */
  border: 0px;
  color: #fff;
  text-shadow: 0 1px rgba(0, 0, 0, 0.1);
  background-color: #4d90fe;
  padding: 17px 0px;
  font-family: roboto;
  font-size: 14px;
  cursor: pointer;
  /* background-image: -webkit-gradient(linear, 0 0, 0 100%,   from(#4d90fe), to(#4787ed)); */
}

.loginmodal-submit:hover {
  /* border: 1px solid #2f5bb7; */
  border: 0px;
  text-shadow: 0 1px rgba(0, 0, 0, 0.3);
  background-color: #357ae8;
  /* background-image: -webkit-gradient(linear, 0 0, 0 100%,   from(#4d90fe), to(#357ae8)); */
}

.loginmodal-container a {
  text-decoration: none;
  color: #666;
  font-weight: 400;
  text-align: center;
  display: inline-block;
  opacity: 0.6;
  transition: opacity ease 0.5s;
}

.login-help {
  font-size: 12px;
}
</style>
