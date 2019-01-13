<template>
    <div>
      <Navbar/>
      <div class="container" style="margin-top: 50px;">
        <h1 style="text-align: center;">Szczegóły oferty</h1>
        <OfferDetails/>
      </div>
    </div>
</template>

<script>
import OfferDetails from "@/components/OfferDetails.vue";
import Navbar from "@/components/Navbar.vue";

export default {
  name: "home",
  components: {
    OfferDetails,
    Navbar
  }
};
</script>
