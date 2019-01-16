<template>
  <div>
    <Navbar/>
    <div>Wylogowanie nastąpi za {{ counter }}</div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  name: "home",
  data() {
    return {
      counter: 3,
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
    if (localStorage.getItem("token")) {
      this.startCounter();
      localStorage.removeItem("profile");
      localStorage.removeItem("token");
    } else {
      this.$router.push("/");
    }
  },
  components: {
    Navbar
  }
};
</script>
