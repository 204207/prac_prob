<template>
  <div>
    DETAILS {{ offer.price }}
    <CreateOrderButton :offer="offer" />
  </div>
</template>

<script>
import CreateOrderButton from "@/components/CreateOrderButton.vue";
import axios from "axios";

export default {
  name: "OfferListItem",
  data: function() {
    return {
      offer: null
    };
  },
  mounted: function() {
    axios
      // eslint-disable-next-line
      .get(
        "http://185.238.73.103:8008/api/offers/" +
          this.$route.params.pathMatch +
          "/?format=json"
      )
      .then(response => (this.offer = response["data"]));
  },
  components: {
    CreateOrderButton
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.offer-item {
  text-decoration: none;
  color: inherit;
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  justify-content: space-evenly;
  background-color: #e0e0e0;
  border: 1px solid grey;
  border-radius: 3px;
  margin: 5px;
}

.offer-item:hover {
  background-color: #e0e0f9;
}
</style>
