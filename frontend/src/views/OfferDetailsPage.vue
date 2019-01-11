<template>
    <div>
      <Navbar/>
      Szczegóły oferty
      <OfferDetails/>
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
