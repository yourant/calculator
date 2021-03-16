<style lang="scss" scoped>
.checkout {
    margin-top:13%;
}
</style>>


<template>
    <v-container>
        <v-row class="checkout">
            <v-col sm="6" offset-sm="3">
                <v-stepper v-model="step">
                    <v-stepper-header>
                      <v-stepper-step step="1" :complete="step > 1"/>
                            <v-divider />
                      <v-stepper-step step="2" :complete="step > 2"/> 
                            <v-divider />
                      <v-stepper-step step="3"/> 

                    </v-stepper-header>

                    <v-stepper-items>
                        <ContactInfo 
                            :data="data"
                            :rules="rules"
                            :next="next"
                        />
                        <ShippingInfo 
                            :data="data"
                            :rules="rules"
                            :next="next"
                            :previouis="previous"
                        />
                        <Review
                            :data="data"
                            :submitOrder="submitOrder"
                            :previous="previous"
                        />
                    </v-stepper-items>

                </v-stepper>
            </v-col>
        </v-row>
    </v-container>
</template>




                        // <v-step-content step="1">
                        //     Step 1
                        // </v-step-content>

                        //  <v-step-content step="2">
                        //     Step 2
                        // </v-step-content>
                        
                        // <v-step-content step="3">
                        //     Step 3
                        // </v-step-content>      

<script lang="ts">
import ContactInfo from '@/components/checkout/ContactInfo.vue';
import ShippingInfo from '@/components/checkout/ShippingInfo.vue';
import Review from '@/components/checkout/Review.vue';
import { Component, Vue } from 'vue-property-decorator';

@Component({
  components: {
    ContactInfo,
    ShippingInfo,
    Review,
  },
})

export default class Checkout extends Vue {
    public step: number = 1;
    public data: object = {
        email : '',
        name : '',
        phone: '',
        street: '',
        state: '',
        zip: '',
    };

    public next() {
        this.step += 1;
    }
    public previous() {
        this.step -= 1;
    }
}
</script>