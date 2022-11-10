<template>
  <div>
    <iframe width="100%" height="500px" :src="videoUrl" frameborder="0"></iframe>
    <h1>{{videoTitle}}</h1>
    <h3>{{videoDescription}}</h3>
    <div id="profileBox">
      <img src="" alt="">
      <h3>{{channelTitle}}</h3>
    </div>
    <hr>

  </div>
</template>

<script>
export default {
  name:'VideoDetail',
  props:{
    selectVideo:Object,
  },
  computed:{
    videoId(){
      return this.selectVideo.id.videoId
    },
    videoUrl(){
      return 'https://www.youtube.com/embed/'+this.videoId
    },
    videoTitle(){
      return this.selectVideo.snippet.title
    },
    videoDescription(){
      return this.selectVideo.snippet.description
    },
    channelTitle(){
      return this.selectVideo.snippet.channelTitle
    }
  }
}
</script>

<style>
  #profileBox{
    display: flex;
  }
</style>