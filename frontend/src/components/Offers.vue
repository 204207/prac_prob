<template>
  <div class="offers">
    <h1 style="text-align: center; margin-bottom: 30px;">Oferty</h1>
    <div class="row offers-header">
      <div class="col-sm-3">
        <span>Miejsce załadunku</span>
      </div>
      <div class="col-sm-1"></div>
      <div class="col-sm-3">
        <span>Miejsce rozładunku</span>
      </div>
      <div class="col-sm-1">
        <span>Nadwozie</span>
      </div>
      <div class="col-sm-2">
        <span>Godziny</span>
      </div>
      <div class="col-sm-2">
        <span>Cena</span>
      </div>
    </div>
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
.offers-header {
  margin: 0 auto;
  text-align: center;
}
.offers {
  margin: 50px auto;
  width: 90%;
}
</style>
