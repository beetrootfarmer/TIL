<template>
  <div>
    <ul v-for="(data, idx) in datas" :key="idx">
      <li @click="showVideo(idx)">
        <VideoListItem :data="data"/>
      </li>
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
  name: 'VideoList',
  components:{
    VideoListItem,
  },
  props:{
    datas:Array,
    // console.log(datas)
  },
  methods:{
    showVideo(idx){
      this.$emit('show-video', this.datas[idx])
    }
  }
}
</script>

<style>

</style>