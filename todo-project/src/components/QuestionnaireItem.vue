<script>
export default {
  props: {
    questionnaire: Object,
    index: Number
  },

  methods:{
    suppr: function() {
    this.$emit("suppr", this.index);
  }


  },
}
</script>

<template>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
     <div class="checkbox btn-group">
      <label>
        <div>{{ questionnaire.name }}</div>
      </label>
      <span>
        <button class="btn btn-danger" @click="suppr()">Supprimer</button>
        <router-link :to="/questions/+questionnaire.id" class="btn btn-primary">Voir mes questions</router-link>
      </span>
    </div>

   
    

</template>