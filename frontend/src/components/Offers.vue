<template>
  <div class="offers">
    <h1>Oferty</h1>
    <OfferListItem v-for="offer in offers" :key="offer.id" v-bind:offer="offer"/>
  </div>
</template>

<script>
import OfferListItem from "./OfferListItem.vue";
import axios from "axios";

export default {
  name: "Offers",
  data: function() {
    return {
      offers: null
    };
  },
  mounted: function() {
    axios
      .get("http://185.238.73.103:8008/api/offers/?format=json")
      .then(response => (this.offers = response["data"]));
  },
  components: {
    OfferListItem
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.offers {
  margin: 0 auto;
  width: 90%;
}
</style>
