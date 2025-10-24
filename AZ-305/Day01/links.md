# AZ-305 - Designing Microsoft Azure Infrastructure Solutions
Links that where shared during the course:

## Course Syllabus
https://learn.microsoft.com/en-us/credentials/certifications/exams/az-305/

<br>

### Design identity, governance, and monitor solutions
- [Module](https://learn.microsoft.com/en-us/training/paths/design-identity-governance-monitor-solutions/)

<br>

<B>M01-01 Design for governance</B>
- [Why is governance important](https://learn.microsoft.com/azure/cloud-adoption-framework/govern/methodology)
- [Azure governance documentation](https://learn.microsoft.com/azure/governance/)
- [Overview of Azure subscriptions, management groups, and resources](https://learn.microsoft.com/learn/modules/azure-architecture-fundamentals/overview)
- [Organize your Azure resources effectively](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources?tabs=AzureManagementGroupsAndHierarchy)
- [Azure Naming Abbreviations](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations)

<br>

<B>M01-02 Design for management groups</B>
- [What are Azure management groups](https://learn.microsoft.com/azure/governance/management-groups/overview)

<br>

<B>M01-03 Design for Azure subscriptions</B>
- [Subscription decision guide](https://learn.microsoft.com/en-gb/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-subscriptions)

<br>

<B>M01-04 Design for resource groups</B>
- [What is Azure Resource Manager](https://docs.microsoft.com/azure/azure-resource-manager/management/overview)
- [What is a resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#what-is-a-resource-group)

<br>

<B>M01-05 Design for resource tagging</B>
- [Resource naming and tagging decision guide](https://learn.microsoft.com/azure/cloud-adoption-framework/decision-guides/resource-tagging/)
- [Define your tagging strategy](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-best-practices/resource-tagging)
- [Resource tagging patterns](https://learn.microsoft.com/azure/cloud-adoption-framework/decision-guides/resource-tagging/?toc=/azure/azure-resource-manager/management/toc.json#resource-tagging-patterns)
<br>


<B>M01-06 Design for Azure Policy and RBAC</B>
- [What is Azure Policy](https://learn.microsoft.com/azure/governance/policy/overview)
- [Azure Built-in Policy List](https://learn.microsoft.com/azure/governance/policy/samples/built-in-policies#general)
- [Create and manage policies to enforce compliance](https://learn.microsoft.com/azure/governance/policy/tutorials/create-and-manage)
- [Only grant the access users need](https://learn.microsoft.com/azure/role-based-access-control/best-practices#only-grant-the-access-users-need)
- [Limit the number of subscription owners](https://learn.microsoft.com/azure/role-based-access-control/best-practices#limit-the-number-of-subscription-owners)
- [Microsoft Entra Privileged Identity Management](https://learn.microsoft.com/azure/role-based-access-control/best-practices#use-azure-ad-privileged-identity-management)
- [Assign roles to groups, not users](https://learn.microsoft.com/azure/role-based-access-control/best-practices#assign-roles-to-groups-not-users)
- [Manage access to an Azure subscription by using Azure role-based access control](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-setup-guide/manage-access)
- [Enterprise policy as code documentation](https://azure.github.io/enterprise-azure-policy-as-code/)
- [Enterprise policy as code github repository](https://azure.github.io/enterprise-azure-policy-as-code/)

<br>


<B>M01-07 Design for Landing Zones</B>
- [What are Azure Landing Zones](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/)
- [Choose the best Azure landing zone to support your requirements for cloud operations](https://learn.microsoft.com/learn/modules/cloud-adoption-framework-ready/)
- [Azure Landing Zones - Community calls](https://github.com/Azure/Enterprise-Scale/wiki/Community-Calls)
- [Build a cloud governance strategy on Azure - Learn | Microsoft Docs](https://learn.microsoft.com/learn/modules/build-cloud-governance-strategy-azure/)
- [Introduction to the Microsoft Azure Well Architected Framework](https://learn.microsoft.com/training/modules/azure-well-architected-introduction/)

<br>

### Design a compute solution
- [Module](https://learn.microsoft.com/training/modules/design-compute-solution/)

<br>

<B>M02-01 Choose a compute solution </B>
- [Choose an Azure compute service for your application](https://learn.microsoft.com/azure/architecture/guide/technology-choices/compute-decision-tree)

<br>

<B>M02-02 Design for Azure virtual machine solutions</B>
- [Responsibility](https://learn.microsoft.com/azure/security/fundamentals/shared-responsibility)
- [VM sizes](https://learn.microsoft.com/azure/virtual-machines/sizes)
- [Azure Disks](https://learn.microsoft.com/azure/virtual-machines/managed-disks-overview)
- [Virtual machines in Azure](https://learn.microsoft.com/azure/virtual-machines/overview)
- [Azure Well-Architected Framework perspective on Virtual Machines and scale sets](https://learn.microsoft.com/azure/well-architected/service-guides/virtual-machines)
- [Azure calculater](https://aka.ms/vm-selector)
- [VM Scale Set high availability](https://learn.microsoft.com/azure/virtual-machines/availability)
- [Image Gallery](https://learn.microsoft.com/azure/virtual-machines/shared-image-galleries)

<br>

<B>M02-03 Design for Azure Batch solutions</B>
- [What is Azure Batch](https://learn.microsoft.com/azure/batch/batch-technical-overview)
- [Best practices](https://learn.microsoft.com/azure/batch/best-practices)
- [Quota and limits](https://learn.microsoft.com/en-gb/azure/batch/batch-quota-limit)

<br>

<B>M02-04 Design for Azure App Services solutions</B>
- [Azure App Service plan](https://learn.microsoft.com/azure/app-service/overview-hosting-plans#how-much-does-my-app-service-plan-cost)
- [Azure App Service plan costs](https://learn.microsoft.com/en-gb/azure/app-service/overview-manage-costs#understand-the-full-billing-model-for-azure-app-service)
- [Deployment slots](https://learn.microsoft.com/azure/app-service/deploy-staging-slots)
- [Custom Container](https://learn.microsoft.com/azure/app-service/quickstart-custom-container?tabs=dotnet&pivots=container-linux)
- [What are WebJobs](https://learn.microsoft.com/azure/app-service/webjobs-create)

<br>

<B>M02-05 Design for Azure Container Instances solutions</B>
- [Azure Container Instances](https://learn.microsoft.com/azure/container-instances/container-instances-overview)
- [Security considerations for container instances]()
- [Containers vs. virtual machines](https://learn.microsoft.com/virtualization/windowscontainers/about/containers-vs-vm)

<br>

<B>M02-06 Design for Azure Kubernetes Service solutions</B>
- [Concept AKS](https://learn.microsoft.com/azure/aks/concepts-clusters-workloads)
- [What is AKS](https://learn.microsoft.com/azure/aks/intro-kubernetes)
- [AKS Costs](https://azure.microsoft.com/pricing/details/kubernetes-service/)
- [Scaling options](https://learn.microsoft.com/azure/aks/concepts-scale)
- [Isolation](https://learn.microsoft.com/azure/aks/operator-best-practices-cluster-isolation)
- [AKS best practices](https://learn.microsoft.com/azure/aks/best-practices)
- [Baseline architecture](https://learn.microsoft.com/en-gb/azure/architecture/reference-architectures/containers/aks/baseline-aks?toc=%2Fazure%2Faks%2Ftoc.json&bc=%2Fazure%2Faks%2Fbreadcrumb%2Ftoc.json)

<br>

<B>M02-07 Design for Azure Functions</B>
- [Azure Functions Overview](https://learn.microsoft.com/azure/azure-functions/functions-overview)
- [Scenarios to use Azure Function](https://learn.microsoft.com/azure/azure-functions/functions-scenarios)
- [Durable functions](https://learn.microsoft.com/azure/azure-functions/durable/durable-functions-overview)
- [Best practices for reliable Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-best-practices)
- [Compare Azure Functions and Azure logic apps](https://learn.microsoft.com/azure/azure-functions/functions-compare-logic-apps-ms-flow-webjobs#compare-azure-functions-and-azure-logic-apps)


<br>

<B>M02-08 Design for Azure Logic App solutions</B>
- [Logic App overview](https://learn.microsoft.com/azure/logic-apps/logic-apps-overview)
- [Differences between a Logic App and Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-compare-logic-apps-ms-flow-webjobs#compare-azure-functions-and-azure-logic-apps)
- [Azure Logic App Documentation](https://learn.microsoft.com/azure/logic-apps/)

<br>
