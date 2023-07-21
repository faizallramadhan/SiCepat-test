Feature:

Scenario:
  * url 'https://jsonplaceholder.typicode.com/posts'
#   * path 'users'
  * method get
  * status 200
  * match response.id == '#number'
  * match response.title == '#string'
  * match response.body == '#string'
  * match response.userId == !null