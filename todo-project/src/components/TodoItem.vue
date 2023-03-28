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
  methods:{
    /*
    edit: function() {
        this.question.editing = true;
    },
    applyEdit: function() {
        this.question.title = this.editText;
        this.question.editing = false;
    },
    suppr: function() {
    this.$emit("suppr", this.index);
    }*/

  },
  /*
  emits: ["suppr"]*/
}
</script>

<template>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
     <div class="checkbox">
        <label>
        <!-- 
            <input type="checkbox"
                v-model="question.checked">
            <div v-if="question.editing" class="editing">
                <input type="text" v-model="editText" @keyup.enter="applyEdit()" @blur="applyEdit()" />
            </div>-->
            <div>
                {{ question.title }}
            </div>
        </label>
        <span class="input-group-btn">
            <input class="btn btn-danger" value="Supprimer" type="button" > <!-- @click="suppr()"-->

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