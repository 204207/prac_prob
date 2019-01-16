<template>
  <div>
    <Navbar/>
    <div class="container">
    <Offers/>
    </div>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Offers from "@/components/Offers.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "home",
  components: {
    Offers,
    Navbar,
    Footer
  }
};
</script>
