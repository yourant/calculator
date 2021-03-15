<template>
<div>
    <v-row v-for ="product in products"
    :key="product.asin">

    <HorizontalProduct :product="product"
                btnAction="remove"
    />

    </v-row>
</div>
</template>


<script lang="ts">
import HorizontalProduct from '@/components/cart/HorizontalProduct.vue';
import { Vue, Component } from 'vue-property-decorator';
import { readProductDetail } from '@/store/main/getters';
import { dispatchSetProductDetail } from '@/store/main/actions';
import { commitAddToCart } from '@/store/main/mutations';

@Component({
  components: {
    HorizontalProduct,
  },
})
export default class ProductList extends Vue {
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
