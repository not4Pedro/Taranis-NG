import ApiService from '@/services/api_service'

export function getAllOSINTSourceGroupsAssess () {
  return ApiService.get('/assess/osint-source-groups')
}

export function getOSINTSourceGroupsList () {
  return ApiService.get('/assess/osint-source-group-list')
}

export function getOSINTSourcesList () {
  return ApiService.get('/assess/osint-sources-list')
}

export function getManualOSINTSources () {
  return ApiService.get('/assess/manual-osint-sources')
}

export function buildFilterQuery (group_id, filter_data) {
  var filter = '?limit=' + filter_data.limit
  if (typeof filter_data.filter.important !== 'undefined') {
    filter += '&important=' + filter_data.filter.important
  }
  if (typeof filter_data.filter.in_analyze !== 'undefined') {
    filter += '&in_analyze=' + filter_data.filter.in_analyze
  }
  if (typeof filter_data.filter.relevant !== 'undefined') {
    filter += '&relevant=' + filter_data.filter.relevant
  }

  if (filter_data.offset !== 0) {
    filter += '&offset=' + filter_data.offset
  }
  if (filter_data.filter.range !== '') {
    filter += '&range=' + filter_data.filter.range
  }
  if (group_id !== '') {
    filter += '&group=' + group_id
  }
  if (filter_data.filter.search !== '') {
    filter += '&search=' + filter_data.filter.search
  }
  return filter
}

export function getNewsItemAggregateByGroup (group_id, filter_data) {
  const filter = buildFilterQuery(group_id, filter_data)
  return ApiService.get(`/assess/news-item-aggregates${filter}`)
}

export function getNewsItemsAggregates (filter_data) {
  const filter = buildFilterQuery('', filter_data)
  return ApiService.get(`/assess/news-item-aggregates${filter}`)
}

export function getNewsItems (filter_data) {
  const filter = buildFilterQuery('', filter_data)
  return ApiService.get(`/assess/news-items${filter}`)
}

export function getTopStories () {
  return ApiService.get('/assess/top-stories')
}

export function addNewsItem (data) {
  return ApiService.post('/assess/news-items', data)
}

export function getNewsItemAggregate (aggregate_id) {
  return ApiService.get(`/assess/news-item-aggregates/${aggregate_id}`)
}

export function voteNewsItemAggregate (group_id, aggregate_id, vote) {
  return ApiService.put(`/assess/news-item-aggregates/${aggregate_id}`, { group_id: group_id, vote: vote })
}

export function readNewsItemAggregate (group_id, aggregate_id) {
  return ApiService.put(`/assess/news-item-aggregates/${aggregate_id}`, { group_id: group_id, read: true })
}

export function deleteNewsItemAggregate (aggregate_id) {
  return ApiService.delete(`/assess/news-item-aggregates/${aggregate_id}`)
}

export function importantNewsItemAggregate (group_id, aggregate_id) {
  return ApiService.put(`/assess/news-item-aggregates/${aggregate_id}`, {
    group_id: group_id,
    important: true
  })
}

export function groupAction (data) {
  return ApiService.put('/assess/news-item-aggregates-group-action', data)
}

export function saveNewsItemAggregate (group_id, aggregate_id, title, description, comments) {
  return ApiService.put(`/assess/news-item-aggregates/${aggregate_id}`, {
    group_id: group_id,
    title: title,
    description: description,
    comments: comments
  })
}

export function getNewsItem (news_item_id) {
  return ApiService.get(`/assess/news-items/${news_item_id}`)
}

export function voteNewsItem (group_id, news_item_id, vote) {
  return ApiService.put(`/assess/news-items/${news_item_id}`, { group_id: group_id, vote: vote })
}

export function readNewsItem (group_id, news_item_id) {
  return ApiService.put(`/assess/news-items/${news_item_id}`, { group_id: group_id, read: true })
}

export function deleteNewsItem (group_id, news_item_id) {
  return ApiService.delete(`/assess/news-items/${news_item_id}`)
}

export function importantNewsItem (group_id, news_item_id) {
  return ApiService.put(`/assess/news-items/${news_item_id}`, { group_id: group_id, important: true })
}
