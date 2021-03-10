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
import { commitSetProductDetail } from '@/store/main/mutations';
import {readProductDetail} from '@/store/main/getters';

@Component({
  components: {
    ProductCard,
  },
})
export default class ProductList extends Vue {

  public product = {};
  public products: object = [
        {
          id: 1,
          name: 'Charity Ball',
          category: 'Fundraising',
          description: 'Spend an elegant night of dinner and dancing',
          featuredImage: 'https://placekitten.com/500/500',
          images: [
            'https://placekitten.com/500/500',
            'https://placekitten.com/500/500',
            'https://placekitten.com/500/500',
          ],
          location: '1234 Fancy Ave',
          date: '2019-12-25',
          time: '11:30',
        },
        {
          id: 2,
          name: 'Rescue Center Goods Drive',
          category: 'Adoptions',
          description: 'Come to our donation drive to help us replenish our stock of pet food, toys, bedding, etc. We will have live bands, games, food trucks, and much more.',
          featuredImage: 'https://placekitten.com/500/500',
          images: [
            'https://placekitten.com/500/500',
          ],
          location: '1234 Dog Alley',
          date: '2019-11-21',
          time: '12:00',
        },
        {
          id: 3,
          name: 'Rescue Center Goods Drive',
          category: 'Adoptions',
          description: 'Come to our donation drive to help us replenish our stock of pet food, toys, bedding, etc. We will have live bands, games, food trucks, and much more.',
          featuredImage: 'https://placekitten.com/500/500',
          images: [
            'https://placekitten.com/500/500',
          ],
          location: '1234 Dog Alley',
          date: '2019-11-21',
          time: '12:00',
        },
                {
          id: 4,
          name: 'Rescue Center Goods Drive',
          category: 'Adoptions',
          description: 'Come to our donation drive to help us replenish our stock of pet food, toys, bedding, etc. We will have live bands, games, food trucks, and much more.',
          featuredImage: 'https://placekitten.com/500/500',
          images: [
            'https://placekitten.com/500/500',
          ],
          location: '1234 Dog Alley',
          date: '2019-11-21',
          time: '12:00',
        },

  ];

  get loadProductDetail() {
    return readProductDetail(this.$store);
  }
}

</script>

