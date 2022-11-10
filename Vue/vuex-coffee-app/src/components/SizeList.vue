<template>
  <div id="sizeListItems">
    <div 
      class="selectBox"
      >
      <h3>사이즈를 고르세요</h3>
      <SizeListItems 
        :size-list="sizeList"
        />
    </div>
  </div>
</template>

<script>
import SizeListItems from '@/components/SizeListItems'
export default {
  components: {
    SizeListItems,
  },

  methods:{

  },
  computed:{
    sizeList(){
      return this.$store.state.sizeList
    }
  }
}
</script>

<style>

</style>