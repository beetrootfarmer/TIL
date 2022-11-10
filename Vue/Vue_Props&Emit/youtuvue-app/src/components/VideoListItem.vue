<template>
  <div id="videoList">
    <img :src="videoUrl" alt="">
    <div id="videoText">
      <li id="listTitle">
          {{ data.snippet.title}}
      </li>
      <li  id="listTitle">
        {{ description}}
      </li>
    </div>
  </div>
</template>

<script>
export default {
  name:'VideoListItem',
  props:{
    data: Object,
  },
  computed:{
    videoUrl(){
      return this.data.snippet.thumbnails.default.url
    },
    description(){
      return this.data.snippet.description
    }
  },
}
</script>

<style>
  #videoList{
    display: flex;
    justify-content: flex-start;
  }
  #listTitle{
    margin: 10px;
  }
  #videoText{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
</style>