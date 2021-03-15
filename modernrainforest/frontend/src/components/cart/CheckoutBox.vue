<template>
    <div>
        <v-card outlined>
            <v-card-title>Payment Details</v-card-title>
            <v-card-text>
                <v-text-field label="name"/>
                <v-text-field  label="email"/>
                <p>Total: $999</p>
                <v-btn color="primary" to="/checkout">
                    Checkout
                </v-btn>
            </v-card-text>
        </v-card>
    </div>
</template>


<script lang="ts">


import { Component, Vue } from 'vue-property-decorator';

@Component
export default class CheckoutBox extends Vue {

}
</script>
