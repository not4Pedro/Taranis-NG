import { apiService } from '@/main'

export function getAllProducts(filter_data) {
  const filter = apiService.getQueryStringFromNestedObject(filter_data)
  return apiService.get(`/publish/products?${filter}`)
}

export function createProduct(data) {
  return apiService.post('/publish/products', data)
}

export function updateProduct(data) {
  return apiService.put(`/publish/products/${data.id}`, data)
}

export function getProduct(product) {
  return apiService.get(`/publish/products/${product.id}`)
}

export function deleteProduct(product) {
  return apiService.delete(`/publish/products/${product.id}`)
}

export function publishProduct(product_id, publisher_id) {
  return apiService.post(
    `/publish/products/${product_id}/publishers/${publisher_id}`,
    {}
  )
}
