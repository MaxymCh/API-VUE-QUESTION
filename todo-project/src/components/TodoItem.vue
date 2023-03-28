<script>
export default {
  props: {
    todo: Object,
    index: Number
  },
  data() {
    return {
      editText: this.todo.text,
    };
  },
  methods:{
    edit: function() {
        this.todo.editing = true;
    },
    applyEdit: function() {
        this.todo.text = this.editText;
        this.todo.editing = false;
    },
    suppr: function() {
    this.$emit("suppr", this.index);
    }

  },
  emits: ["suppr"]
}
</script>

<template>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
     <div class="checkbox">
        <label>
            <input type="checkbox"
                v-model="todo.checked">
            <div v-if="todo.editing" class="editing">
                <input type="text" v-model="editText" @keyup.enter="applyEdit()" @blur="applyEdit()" />
            </div>
            <div v-else>
                {{ todo.text }}
            </div>
        </label>
        <span class="input-group-btn">
            <input class="btn btn-danger" value="Supprimer" type="button" @click="suppr()">

        </span>
        <span class="input-group-btn">
            <button @click="edit()" v-if="!todo.editing">Modifier</button>

        </span>
        <div class="alert alert-success" v-if="todo.checked">
            Done
        </div>

    </div>
   
    

</template>