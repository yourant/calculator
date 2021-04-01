<template>
    <v-stepper-content step="2">

        <v-text-field 
            v-model="data.street"
            label="Street Address"
            required
        />
        <v-text-field 
            v-model="data.state"
            label="State"
            required
        />
        <v-text-field 
            v-model="data.zip"
            label="Zip"
            required
        />

        <v-btn color="primary"  @click="next">
        Continue
        </v-btn>

        <v-btn text @click="previous">
        Go Back
        </v-btn>

    </v-stepper-content>
</template>



<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class ShippingInfo extends Vue {
  @Prop() public next !: () => void;
  @Prop() public previous !: () => void;
  @Prop(Object) public data: object = [];

}

</script>


