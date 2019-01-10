<template>
  <div id="login-modal" role="dialog">
    <div class="loginmodal-container">
      <h1>Rejestracja</h1>
      <br>
      <form @submit.prevent="register">
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
          <input
            type="text"
            v-model="email"
            name="email"
            placeholder="E-mail"
            class="form-control"
            :class="{ 'is-invalid': submitted && !email }"
          >
          <input
            type="text"
            v-model="firstName"
            name="firstName"
            placeholder="Imię"
            class="form-control"
            :class="{ 'is-invalid': submitted && !firstName }"
          >
          <input
            type="text"
            v-model="lastName"
            name="lastName"
            placeholder="Nazwisko"
            class="form-control"
            :class="{ 'is-invalid': submitted && !lastName }"
          >
          <input
            type="text"
            v-model="phoneNumber"
            name="phoneNumber"
            placeholder="Numer telefonu"
            class="form-control"
            :class="{ 'is-invalid': submitted && !phoneNumber }"
          >
          <input
            type="text"
            v-model="company"
            name="company"
            placeholder="Nazwa firmy"
            class="form-control"
            :class="{ 'is-invalid': submitted && !company }"
          >
          <input
            type="text"
            v-model="nipNumber"
            name="nipNumber"
            placeholder="NIP"
            class="form-control"
            :class="{ 'is-invalid': submitted && !nipNumber }"
          >
          <input
            type="text"
            v-model="country"
            name="country"
            placeholder="Kraj"
            class="form-control"
            :class="{ 'is-invalid': submitted && !country }"
          >
          <input
            type="text"
            v-model="city"
            name="city"
            placeholder="Miasto"
            class="form-control"
            :class="{ 'is-invalid': submitted && !city }"
          >
          <input
            type="text"
            v-model="postCode"
            name="postCode"
            placeholder="Kod pocztowy"
            class="form-control"
            :class="{ 'is-invalid': submitted && !postCode }"
          >
          <input
            type="text"
            v-model="street"
            name="street"
            placeholder="Ulica"
            class="form-control"
            :class="{ 'is-invalid': submitted && !street }"
          >
          <div v-show="submitted && !password" class="invalid-feedback">Hasło jest wymagane!</div>
          <input
            type="submit"
            name="register"
            class="login loginmodal-submit"
            v-model="registerBtnTxt"
          >
        </div>
      </form>

      <div class="login-help">Masz już konto?
        <br>
        <router-link to="/zaloguj">Zaloguj się</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      registerBtnTxt: "Zarejestruj się",
      submitted: false,
      username: "",
      password: "",
      email: "",
      firstName: "",
      lastName: "",
      phoneNumber: "",
      company: "",
      nipNumber: "",
      country: "",
      city: "",
      postCode: "",
      street: ""
    };
  },
  methods: {
    register: function() {
      this.submitted = true;

      var registerJson = {
        user: {
          username: this.username,
          password: this.password
        },
        address: {
          street: this.street,
          post_code: this.postCode,
          place: this.city,
          country: this.country
        },
        name: this.firstName,
        surname: this.lastName,
        email: this.email,
        phone_number: this.phoneNumber,
        company: this.company,
        tax_number: this.nipNumber
      };

      axios
        .post("http://185.238.73.103:8008/api/profiles/", registerJson)
        .then(response => {
          this.registerBtnTxt = "Konto utworzone!";
          this.$router.push("/zaloguj");
          console.log(response);
        })
        .catch(() => {
          this.registerBtnTxt = "Rejestracja nie powiodła się!";
        });
    }
  }
};
</script>

<style scoped>
@import url(http://fonts.googleapis.com/css?family=Roboto);

/****** LOGIN MODAL ******/
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
