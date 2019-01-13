<template>
  <div>
    <Navbar/>
    <div class="container">
      <Orders/>
    </div>

    <Footer/>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import Orders from "@/components/Orders.vue";

export default {
  components: {
    Navbar,
    Footer,
    Orders
  }
};
</script>
