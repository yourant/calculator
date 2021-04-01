<style lang="scss" scoped>
.sidebar {
    margin-top:13%;
}
</style>>

<template>
    <v-container>
        <v-row>
            <v-col class="sidebar" md="3" offset-lg="1">
                <Sidebar />
            </v-col>

            <v-col  md="9" lg="7">
                <ProductDisplay />
            </v-col>
        </v-row>
    </v-container>
</template>



<script lang="ts">
import ProductDisplay from '@/components/shop/ProductDisplay.vue';
import Sidebar from '@/components/shop/Sidebar.vue';
import { Component, Vue } from 'vue-property-decorator';

@Component({
  components: {
    ProductDisplay,
    Sidebar,
  },
})

export default class Shop extends Vue {

}
</script>