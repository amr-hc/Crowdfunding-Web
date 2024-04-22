<template>

    <div class="container my-5">
        <h2>Categories</h2>
        <hr class="my-4 bg-dark w-25">
        <form @submit.prevent="addCategory">
            <div class="row">
                <div class="mb-3 col">
                    <label for="name" class="form-label">Name:</label>
                    <input type="text" required id="name" v-model="newCategory.name" class="form-control">
                </div>
                <div class="mb-3 col">
                    <label for="description" class="form-label">Description:</label>
                    <input type="text" required maxlength="50" id="description" v-model="newCategory.description"
                        class="form-control">
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Add Category</button>
        </form>
        <hr class="my-4">
        <div class="d-flex flex-wrap" v-if="categories.length > 0">
            <div class="cat-card" v-for="category in categories" :key="category.id"
                @mouseenter="showDeleteIcon(category)" @mouseleave="hideDeleteIcon(category)">
                <p>{{ category.name }}</p>
                <p class="text-white-50">{{ category.description }}</p>
                <button v-if="category.showDeleteIcon" @click="confirmDelete(category)" class="delete-btn">
                    <i class="fas fa-trash-alt"></i>
                </button>
            </div>

        </div>

        <p v-else>No categories found.</p>

        <h2 class="mt-5">Tags</h2>
        <hr class="my-4 bg-dark w-25">
        <form @submit.prevent="addTag">
            <div class="mb-3">
                <label for="tagName" class="form-label">Tag Name:</label>
                <input type="text" required maxlength="50" id="tagName" v-model="newTag.tagName" class="form-control">
            </div>
            <button type="submit" class="btn btn-primary">Add Tag</button>
        </form>
        <hr class="my-4">

        <div class="d-flex flex-wrap" v-if="tags.length > 0">
            <div class="cat-card" v-for="tag in tags" :key="tag.id" @mouseenter="showDeleteIcon(tag)"
                @mouseleave="hideDeleteIcon(tag)">
                <p>{{ tag.tagName }}</p>
                <button v-if="tag.showDeleteIcon" @click="confirmDeleteTag(tag)" class="delete-btn">
                    <i class="fas fa-trash-alt"></i>
                </button>
            </div>
        </div>
        <p v-else>No tags found.</p>



    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "CategoryTags",
    data() {
        return {
            categories: [],
            newCategory: {
                name: '',
                description: ''
            },
            tags: [],
            newTag: {
                tagName: ''
            }
        };
    },
    created() {
        this.fetchCategories();
        this.fetchTags();
    },
    methods: {
        fetchCategories() {
            axios.get('http://127.0.0.1:8000/api/categories/')
                .then(response => {
                    this.categories = response.data;
                })
                .catch(error => {
                    console.error('Error fetching categories:', error);
                });
        },
        fetchTags() {
            axios.get('http://127.0.0.1:8000/tags/')
                .then(response => {
                    this.tags = response.data;
                })
                .catch(error => {
                    console.error('Error fetching tags:', error);
                });
        },
        addCategory() {
            axios.post('http://127.0.0.1:8000/api/categories/', this.newCategory)
                .then(response => {
                    console.log('Category added successfully:', response.data);
                    // Clear the form and fetch updated categories
                    this.newCategory = {
                        name: '',
                        description: ''
                    };
                    this.fetchCategories();
                })
                .catch(error => {
                    console.error('Error adding category:', error);
                });
        },
        addTag() {
            axios.post('http://127.0.0.1:8000/tags/', this.newTag)
                .then(response => {
                    console.log('Tag added successfully:', response.data);
                    // Clear the form and fetch updated tags
                    this.newTag = {
                        tagName: ''
                    };
                    this.fetchTags();
                })
                .catch(error => {
                    console.error('Error adding tag:', error);
                });
        },
        deleteCategory(category) {
            axios.delete(`http://127.0.0.1:8000/api/categories/${category.id}`)
                .then(() => {
                    console.log('Category deleted successfully');
                    this.fetchCategories();
                })
                .catch(error => {
                    console.error('Error deleting category:', error);
                });
        },
        deleteTag(tag) {
            axios.delete(`http://127.0.0.1:8000/tags/${tag.id}`)
                .then(() => {
                    console.log('Tag deleted successfully');
                    this.fetchTags();
                })
                .catch(error => {
                    console.error('Error deleting tag:', error);
                });
        },
        confirmDelete(category) {
            if (confirm(`Are you sure you want to delete the category "${category.name}"?`)) {
                this.deleteCategory(category);
            }
        },
        confirmDeleteTag(tag) {
            if (confirm(`Are you sure you want to delete the tag "${tag.tagName}"?`)) {
                this.deleteTag(tag);
            }
        }
        , showDeleteIcon(category) {
            category.showDeleteIcon = true;
        },
        hideDeleteIcon(category) {
            category.showDeleteIcon = false;
        }
    }
};
</script>

<style scoped>
.form-control {
    background-color: rgb(45, 52, 61);
}

.form-control:focus {
    background-color: rgb(45, 52, 61);
}


.cat-card {
    backdrop-filter: blur(15px);
    box-shadow: 0px 0 31px 0px rgb(0 0 0 / 10%);
    border-radius: 20px;
    border: 1px solid var(--primary-color-3);
    margin: 10px;
    padding: 10px;
    width: 150px;
    height: auto;
    overflow: hidden;
}

.cat-card p {
    text-align: center;
    margin-top: 10px;
    font-size: 12px;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.delete-btn {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: all 0.2s ease-in-out;
    background-color: rgba(0, 0, 0, 0.5);

}

.delete-btn i {
    z-index: 99;
    color: white;
}

.cat-card:hover .delete-btn {
    opacity: 1;
}
</style>