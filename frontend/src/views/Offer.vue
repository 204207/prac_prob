<template>
    <mdb-container>
        <OfferDetails/>
    </mdb-container>
</template>

<script>
import OfferDetails from "@/components/OfferDetails.vue";
import { mdbContainer } from "mdbvue";

export default {
  name: "home",
  components: {
    OfferDetails,
    mdbContainer
  }
};
</script>
