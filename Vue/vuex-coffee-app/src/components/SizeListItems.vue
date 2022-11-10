<template>
  <div>
    <div 
      id="size" 
      v-for="(size, idx) in sizeList" 
      :key="idx"
      @click="selectdedSize(idx)"
      :class="{'is_selected' : size.selected}"
      >
      <span> {{size.name}} </span>
      <span> {{size.price}}원 </span>
    </div>
  </div>
</template>

<script>
export default {
  name:'SizeListItems',
  props:{
    sizeList: Array,
  },
  methods:{
    selectdedSize(idx){
      console.log(idx)
      this.$store.dispatch('updateSelectedSize', idx)
    }
  }
}
</script>

<style>
  #imgBox{
    width:50px;
    height: 50px;
    border-radius: 10px;
    overflow: hidden;
    
  }
  #thumbnail{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  #size{
    border: groove 2px rgba(25, 138, 95, 0.896);
    border-radius: 10px;
    padding: 30px;
    margin-top: 30px;
    display: flex;
    justify-content: space-between;
    
  }
  .is_selected{
    background-color: rgba(25, 138, 95, 0.896);
    color: white;
    font-size: 1.1em;
  }
  #size:hover{
    background-color: rgba(12, 158, 102, 0.778);
  }
</style>