<style lang="scss" scoped>

</style>

<template>
  <div>
    <h3>Products </h3>
    <v-row>
      <v-col
        sm="6"
        md="4"
        v-for="product in products" :product="product" 
        :key="product.id">
            <!-- <router-link :to="'/product/' + product.id"> -->
        <ProductCard  :addToCart="addToCart" :product="product" />
            <!-- </router-link> -->
      </v-col>
    </v-row>
  </div> 
</template>




<script lang="ts">
import ProductCard from '../ProductCard.vue';
import { Vue, Component } from 'vue-property-decorator';
import { readProductDetail } from '@/store/main/getters';
import { dispatchSetProductDetail } from '@/store/main/actions';
import { commitAddToCart } from '@/store/main/mutations';

@Component({
  components: {
    ProductCard,
  },
})
export default class ProductDisplay extends Vue {
  public category: string = 'Office Products';
  public product = {};
  public itemId = {index:1,quantity:5};

  public async created() {
    await dispatchSetProductDetail(this.$store, this.category);
  }
  public async addToCart(index, quantity = 1) {
    await commitAddToCart(this.itemId)
  }
  get products() {
    return readProductDetail(this.$store);
  }

}

</script>

