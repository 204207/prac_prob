<template>
  <div class="offers">
    <h1>Oferty</h1>
    <OfferItem v-for="offer in offers" :key="offer.id" v-bind:offer="offer"/>
  </div>
</template>

<script>
import OfferItem from "./OfferItem.vue";

export default {
  name: "Offers",
  data: function() {
    return {
      offers: [
        {
          id: 1,
          loading_place: "Łódź",
          destination: "Warszawa"
        },
        {
          id: 2,
          loading_place: "Kielce",
          destination: "Sieradz"
        }
      ]
    };
  },
  components: {
    OfferItem
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
