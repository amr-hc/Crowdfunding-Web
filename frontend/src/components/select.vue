<template>
  <select ref="select" class="form-control select2" multiple="multiple" style="width: 100%;"></select>
</template>

<script>
import $ from 'jquery'; // Import jQuery
import 'select2'; // Import Select2
import { onMounted, onBeforeUnmount } from 'vue'; // Import Vue lifecycle hooks

export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  setup() {
    onMounted(() => {
      $('.select2').select2({
            data: ["Piano", "Flute", "Guitar", "Drums", "Photography"],
            tags: true,
            maximumSelectionLength: 10,
            tokenSeparators: [',', ' '],
            placeholder: "Select or type keywords",
         
        });
    });

    onBeforeUnmount(() => {
      
      const selectElement = document.querySelector('.select2');
      if (selectElement) {
        $(selectElement).select2('destroy');
      }
    });
  }
};
</script>
