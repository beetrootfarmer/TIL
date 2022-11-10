<template>
  <div id="optionListItems">
    <div 
      class="selectBox"
      >
      <h3>옵션을 고르세요</h3>
      <div v-for="(option, idx) in optionList" :key="idx">
        <OptionListItems 
          :selectedOption="option" :idx="idx"
          />
      </div>
    </div>
  </div>
</template>

<script>
import OptionListItems from '@/components/OptionListItems'
export default {
    name:'OptionList',
    components:{
        OptionListItems,
    },
    computed:{
    optionList(){
      return this.$store.state.optionList
    }
  }
}
</script>

<style>

</style>