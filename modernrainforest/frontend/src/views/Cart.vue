<style lang="scss" scoped>
.cart {
    margin-top:13%;
}
</style>>

<template>
    <v-container>
        <v-row class="cart">
            <v-col sm="8" md="5" offset-md="2" lg="4" offset-lg="3">
                <ProductList />
            </v-col>
            <v-col sm="4" md="3" order="first" order-small="last">
                <CheckoutBox />
            </v-col>
        </v-row>
    </v-container>
</template>



<script lang="ts">
import ProductList from '@/components/cart/ProductList.vue';
import CheckoutBox from '@/components/cart/CheckoutBox.vue';
import { Component, Vue } from 'vue-property-decorator';

@Component({
  components: {
    ProductList,
    CheckoutBox,
  },
})

export default class Cart extends Vue {

}
</script>