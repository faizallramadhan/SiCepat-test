Feature: Verify API Response 200

Scenario:
  * url 'https://jsonplaceholder.typicode.com/'
  * path 'posts'
  * method get
  * status 200
  * match response[0].id == '#number'
  * match response[0].title == '#string'
  * match response[0].body == '#string'
  * match response[0].userId == '#notnull'
  
