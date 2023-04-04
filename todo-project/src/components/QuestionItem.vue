<script>
export default {
  props: {
    question: Object,
    index: Number
  },
  /*
  data() {
    return {
      editTitle: this.question.title,
    };
  },*/
  methods: {
  suppr: function() {
    this.$emit("suppr", this.index);
  }
},
  /*
  emits: ["suppr"]*/
}
</script>

<template>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
     <div class="checkbox">
        <label>
            <div>
                {{ question.title }}
            </div>
        </label>
        <span class="input-group-btn">
          <input class="btn btn-danger" value="Supprimer" type="button" @click="suppr()">

        </span>
        <span class="input-group-btn">
          <router-link :to="'/question/edit/' + question.id" class="btn btn-primary">Editer la question</router-link>


        </span>
        <!-- 
        <span class="input-group-btn">
            <button @click="edit()" v-if="!question.editing">Modifier</button>

        </span>
        <div class="alert alert-success" v-if="question.checked">
            Done
        </div>-->

    </div>
   
    

</template>