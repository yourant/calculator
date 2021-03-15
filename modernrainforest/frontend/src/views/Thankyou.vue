<style lang="scss" scoped>
.thankyou {
    margin-top:13%;
}
</style>>


<template>
<div class="thankyou">
    <v-overlay :value="overlay" class="flex-column" >
        <p> Processing Order ...</p>
        <v-progress-circular indeterminate size="64" />
    </v-overlay>
    <v-container v-if="!overlay">
            Thank You!
    </v-container>
</div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class Thankyou extends Vue {
    public overlay: boolean = false;
    public timeout() {
        setTimeout(() => this.overlay = false, 2000);
    }
}

</script>

