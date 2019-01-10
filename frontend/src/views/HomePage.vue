<template>
  <mdb-container>
    <Offers/>
  </mdb-container>
</template>

<script>
// @ is an alias to /src
import Offers from "@/components/Offers.vue";

export default {
  name: "home",
  components: {
    Offers
  }
};
</script>
