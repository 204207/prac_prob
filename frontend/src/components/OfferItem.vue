<template>
  <div class="offer-item">
    <p>{{ offer.loading_place }} -> {{ offer.destination }}</p>
  </div>
</template>

<script>
export default {
  name: "Offer Item",
  props: ["offer"]
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
