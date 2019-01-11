<template>
  <div>
    <Navbar/>
    <div>Wylogowanie nastąpi za {{ counter }}</div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import axios from "axios";

export default {
  name: "home",
  data() {
    return {
      counter: 5,
      interval: null
    };
  },
  methods: {
    startCounter: function() {
      this.interval = setInterval(this.countDown, 1000);
    },
    countDown: function() {
      var n = this.counter;
      if (n > 1) {
        this.counter -= 1;
      } else {
        this.interval = null;
        this.$router.push("/");
      }
    }
  },
  mounted: function() {
    axios
      .get(
        "http://185.238.73.103:8008/api/profiles/get_data_profile",
        { username: "auu" },
        {
          headers: {
            Authorization: "Token " + localStorage.getItem("token"),
            "Content-Type": "application/json"
          }
        }
      )
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      });
  },
  components: {
    Navbar
  }
};
</script>
