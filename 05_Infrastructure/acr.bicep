param name string
param location string

resource registry 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: name
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}

var credentials = listCredentials(registry.id, registry.apiVersion)

output loginServer string = registry.properties.loginServer
output username string = credentials.username
output password string = credentials.passwords[0].value
