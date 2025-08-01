param location string
param environmentName string
param orchestratorName string
param ingestionName string
param frontendAppName string
param triageName string
param remediationName string
param reportingName string
param useSampleImages bool = false
param orchestratorImage string = useSampleImages
  ? 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
  : '${registryLoginServer}/orchestrator:latest'
param ingestion_agentsImage string = useSampleImages
  ? 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
  : '${registryLoginServer}/ingestion:latest'
param frontendImage string = useSampleImages
  ? 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
  : '${registryLoginServer}/frontend:latest'
param triage_agentsImage string = useSampleImages
  ? 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
  : '${registryLoginServer}/triage:latest'
param remediation_agentsImage string = useSampleImages
  ? 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
  : '${registryLoginServer}/remediation:latest'
param reporting_agentsImage string = useSampleImages
  ? 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
  : '${registryLoginServer}/reporting:latest'
param minReplicas int = 1
param maxReplicas int = 1
param cpu string = '0.5'
param memory string = '1Gi'
param registryLoginServer string
param registryUsername string
param registryPassword string

resource env 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: environmentName
  location: location
  properties: {}
}

resource orchestrator 'Microsoft.App/containerApps@2023-05-01' = {
  name: orchestratorName
  location: location
  tags: {
    'azd-service-name': 'orchestrator'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: orchestratorName
          image: orchestratorImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource ingestion 'Microsoft.App/containerApps@2023-05-01' = {
  name: ingestionName
  location: location
  tags: {
    // Service name must match azure.yaml for azd deployments
    'azd-service-name': 'ingestion'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: ingestionName
          image: ingestion_agentsImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource frontend 'Microsoft.App/containerApps@2023-05-01' = {
  name: frontendAppName
  location: location
  tags: {
    'azd-service-name': 'frontend'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: frontendAppName
          image: frontendImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource triage 'Microsoft.App/containerApps@2023-05-01' = {
  name: triageName
  location: location
  tags: {
    // Align tag with service name in azure.yaml
    'azd-service-name': 'triage'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: triageName
          image: triage_agentsImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource remediation 'Microsoft.App/containerApps@2023-05-01' = {
  name: remediationName
  location: location
  tags: {
    // Align tag with service name in azure.yaml
    'azd-service-name': 'remediation'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: remediationName
          image: remediation_agentsImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}

resource reporting 'Microsoft.App/containerApps@2023-05-01' = {
  name: reportingName
  location: location
  tags: {
    // Align tag with service name in azure.yaml
    'azd-service-name': 'reporting'
  }
  properties: {
    environmentId: env.id
    configuration: {
      registries: [
        {
          server: registryLoginServer
          username: registryUsername
          passwordSecretRef: 'acr-pwd'
        }
      ]
      secrets: [
        {
          name: 'acr-pwd'
          value: registryPassword
        }
      ]
    }
    template: {
      containers: [
        {
          name: reportingName
          image: reporting_agentsImage
          resources: {
            cpu: json(cpu)
            memory: memory
          }
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
    }
  }
}
