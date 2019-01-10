<template>
  <router-link :to="/oferty/ + offer.id" class="offer-item">
    <div>
      <p>{{ offer.loading_place.place.country }}</p>
      <p>{{ offer.loading_place.place.place }}</p>
    </div>
    <div>
      <p style="font-size: 20px;">>>></p>
    </div>
    <div>
      <p>{{ offer.destination.place.place }}</p>
      <p>{{ offer.destination.place.country }}</p>
    </div>
    <div>
      <p>{{ offer.vehicle.type }}</p>
    </div>
        <div>
      <p>{{ offer.loading_place.date }}</p>
      <p>{{ offer.loading_place.hour }}</p>
    </div>
    <div>
      <p>{{ offer.price }} PLN</p>
    </div>
  </router-link >
</template>

<script>
export default {
  name: "OfferListItem",
  props: ["offer"]
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
