param location string = resourceGroup().location
param containerEnvName string
param orchestratorAppName string
param ingestionAppName string
param frontendAppName string
param triageAppName string
param remediationAppName string
param reportingAppName string
param cosmosAccountName string
param keyVaultName string
param openAiAccountName string
param containerRegistryName string
param orchestratorImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param ingestionImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param frontendImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param triageImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param remediationImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param reportingImage string = 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
param minReplicas int = 1
param maxReplicas int = 1
param cpu string = '0.5'
param memory string = '1Gi'

module keyVault './keyvault.bicep' = {
  name: 'keyVault'
  params: {
    name: keyVaultName
    location: location
  }
}




module cosmos './cosmos.bicep' = {
  name: 'cosmos'
  params: {
    name: cosmosAccountName
    location: location
  }
}

module openai './openai.bicep' = {
  name: 'openai'
  params: {
    name: openAiAccountName
    location: location
  }
}

module containerRegistry './acr.bicep' = {
  name: 'acr'
  params: {
    name: containerRegistryName
    location: location
  }
}

module apps './containerapps.bicep' = {
  name: 'apps'
  params: {
    location: location
    environmentName: containerEnvName
    orchestratorName: orchestratorAppName
    ingestionName: ingestionAppName
    frontendAppName: frontendAppName
    triageName: triageAppName
    remediationName: remediationAppName
    reportingName: reportingAppName
    orchestratorImage: orchestratorImage
    ingestionImage: ingestionImage
    frontendImage: frontendImage
    triageImage: triageImage
    remediationImage: remediationImage
    reportingImage: reportingImage
    minReplicas: minReplicas
    maxReplicas: maxReplicas
    cpu: cpu
    memory: memory
    registryLoginServer: containerRegistry.outputs.loginServer
    registryUsername: containerRegistry.outputs.username
    registryPassword: containerRegistry.outputs.password
  }
}

output containerRegistryLoginServer string = containerRegistry.outputs.loginServer
output containerRegistryUsername string = containerRegistry.outputs.username
output containerRegistryPassword string = containerRegistry.outputs.password
