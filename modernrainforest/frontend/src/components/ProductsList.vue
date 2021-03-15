<style lang="scss" scoped>
  .events {
    margin-top: 10px;
    text-align: center;
    }
</style>

<template>
  <div class="products container">
    <h2 class="subtitle is-3">
      Check out our upcoming products
    </h2>

    <v-row>
      <v-col v-for="product in products" :product="product" :key="product.id">
        <!-- <router-link :to="'/product/' + product.id"> -->
          <ProductCard  :product="product" />
        <!-- </router-link> -->
      </v-col>
    </v-row>
  </div> 
</template>




<script lang="ts">
import ProductCard from './ProductCard.vue';
import { Vue, Component } from 'vue-property-decorator';
import { readProductDetail } from '@/store/main/getters';
import { dispatchSetProductDetail } from '@/store/main/actions';

@Component({
  components: {
    ProductCard,
  },
})
export default class ProductList extends Vue {
  public category: string = 'Office Products';
  public product = {};

  public async created() {
    await dispatchSetProductDetail(this.$store, this.category);
  }

  get products() {
    return readProductDetail(this.$store);
  }

}

</script>

