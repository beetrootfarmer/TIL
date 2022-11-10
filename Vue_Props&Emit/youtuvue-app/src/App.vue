<template>
  <div id="app">
    <div id="main-head">
      <img id="logo-img" width="200px" src="https://user-images.githubusercontent.com/87971876/201000623-db33c95d-6707-4bd1-99e6-a1642ff991ac.png" alt="">
      <TheSearchBar @search-keyword="searchKeyword" />
    </div>
    <VideoDetail v-if="clicked" :selectVideo="selectVideo"/>
    <VideoList :datas="datas" @show-video="showVideo"/>
  </div>
</template>


<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data (){
    return{
      keyword:null,
      datas:null,
      selectVideo:null,
      clicked:false,
    }
  },
  methods:{
    searchKeyword(keyword){
      this.keyword = keyword
      const API_KEY = 'AIzaSyBHwT2_z4Go2ULCt-TxCAzy69ORxGMnlXM'
      const API_URL = `https://www.googleapis.com/youtube/v3/search/?key=${API_KEY}&part=snippet&type=video&q=${keyword}`
      axios.get(API_URL)
          .then((response) => {
            const data = response.data.items
            this.datas = data
            console.log(this.datas)
          })
      console.log(this.keyword)
    },
    showVideo(selected){
      this.selectVideo = selected
      console.log("비디오보여줘",this.selectVideo)
      this.clicked= true
    },
   
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#main-head{
  display: flex;
  justify-content:space-evenly;
  align-items: center;
}
#main-head>img{
  margin-right:5%;
}
#logo-img{
  margin-top: -50px;
  padding: 0;
}
</style>
