<template>
    <v-stepper-content step="1">

        <v-text-field 
            v-model="data.name"
            label="Name"
            required
        />
        <v-text-field 
            v-model="data.email"
            label="E-mail"
            required
        />
        <v-text-field 
            v-model="data.phone"
            label="Phone Number"
            required
        />
        <v-btn color="primary"  @click="next">
        Continue
        </v-btn>
        <v-btn text to="/cart">
        Cancel
        </v-btn>

    </v-stepper-content>
</template>



<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class ContactInfo extends Vue {
  @Prop() public next !: () => void;
  @Prop(Object) public data: object = [];

}

</script>


