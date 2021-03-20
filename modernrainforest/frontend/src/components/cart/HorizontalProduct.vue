<template>
        <v-card :loading="loading"  class="mb-5 pa-4" min-width="60%" outlined>
            <template slot="progress">
                <v-progress-linear color="deep-purple" height="10" indeterminate  ></v-progress-linear>
            </template>

            <v-img height="200" width="200" :src=product.imagelink ></v-img>


            <div class="d-flex flex-column justify-center">
              <v-card-title>{{product.asin}}, {{product.brand}}</v-card-title>
                <v-card-subtitle>
                    {{product.price}}
                </v-card-subtitle>
                <v-btn color="error" class="ml-4" outlined small>
                    <v-icon small left>mdi-minus</v-icon>
                    Remove from Cart
                </v-btn>
            </div>
        </v-card>
</template>


<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class HorizontalProduct extends Vue {
  @Prop(Object) public product !: object | null;
  public loading: boolean = false;
  public selection: number = 1;
  public reserve() {
      this.loading = true;
      setTimeout(() => (this.loading = false), 2000);
    }
}

</script>