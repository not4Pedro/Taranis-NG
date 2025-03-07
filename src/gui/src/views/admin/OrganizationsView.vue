<template>
  <div>
    <DataTable
      v-model:items="organizations.items"
      :add-button="true"
      :header-filter="['tag', 'id', 'name', 'description', 'actions']"
      sort-by-item="id"
      tag-icon="mdi-office-building"
      @delete-item="deleteItem"
      @edit-item="editItem"
      @add-item="addItem"
      @update-items="updateData"
    />
    <EditConfig
      v-if="showForm"
      :config-data="formData"
      :form-format="formFormat"
      :title="editTitle"
      @submit="handleSubmit"
    ></EditConfig>
  </div>
</template>

<script>
import DataTable from '@/components/common/DataTable.vue'
import EditConfig from '@/components/config/EditConfig.vue'
import {
  deleteOrganization,
  createOrganization,
  updateOrganization
} from '@/api/config'
import { useConfigStore } from '@/stores/ConfigStore'
import { notifySuccess, notifyFailure } from '@/utils/helpers'
import { ref, onMounted, computed } from 'vue'
import { useMainStore } from '@/stores/MainStore'
import { storeToRefs } from 'pinia'

export default {
  name: 'OrganizationsView',
  components: {
    DataTable,
    EditConfig
  },
  setup() {
    const store = useConfigStore()
    const mainStore = useMainStore()
    const { organizations } = storeToRefs(store)
    const formData = ref({})
    const edit = ref(false)
    const showForm = ref(false)
    const formFormat = computed(() => [
      {
        name: 'id',
        label: 'ID',
        type: 'text',
        disabled: true
      },
      {
        name: 'name',
        label: 'Name',
        type: 'text',
        rules: [(v) => !!v || 'Required']
      },
      {
        name: 'description',
        label: 'Description',
        type: 'textarea'
      },
      {
        name: 'street',
        label: 'Street',
        parent: 'address',
        type: 'text'
      },
      {
        name: 'city',
        label: 'City',
        parent: 'address',
        type: 'text'
      },
      {
        name: 'zip',
        label: 'Zip',
        parent: 'address',
        type: 'text'
      },
      {
        name: 'country',
        label: 'Country',
        parent: 'address',
        type: 'text'
      }
    ])

    const updateData = () => {
      showForm.value = false

      store.loadOrganizations().then(() => {
        mainStore.itemCountTotal = organizations.value.total_count
        mainStore.itemCountFiltered = organizations.value.items.length
      })
    }

    const editTitle = computed(() => {
      return edit.value
        ? `Edit Organization: '${formData.value['name']}'`
        : 'Add Organization'
    })

    const addItem = () => {
      formData.value = {}
      edit.value = false
      showForm.value = true
    }

    const editItem = (item) => {
      formData.value = item
      edit.value = true
      showForm.value = true
    }

    const handleSubmit = (submittedData) => {
      console.log(submittedData)
      if (edit.value) {
        updateItem(submittedData)
      } else {
        createItem(submittedData)
      }
    }

    const deleteItem = (item) => {
      deleteOrganization(item)
        .then(() => {
          notifySuccess(`Successfully deleted ${item.name}`)
          updateData()
        })
        .catch(() => {
          notifyFailure(`Failed to delete ${item.name}`)
        })
    }

    const createItem = (item) => {
      createOrganization(item)
        .then(() => {
          notifySuccess(`Successfully created ${item.name}`)
          updateData()
        })
        .catch(() => {
          notifyFailure(`Failed to create ${item.name}`)
        })
    }

    const updateItem = (item) => {
      updateOrganization(item)
        .then(() => {
          notifySuccess(`Successfully updated ${item.name}`)
          updateData()
        })
        .catch(() => {
          notifyFailure(`Failed to update ${item.name}`)
        })
    }

    onMounted(() => {
      updateData()
    })

    return {
      organizations,
      formFormat,
      formData,
      editTitle,
      showForm,
      addItem,
      editItem,
      handleSubmit,
      updateData,
      deleteItem,
      createItem,
      updateItem
    }
  }
}
</script>
