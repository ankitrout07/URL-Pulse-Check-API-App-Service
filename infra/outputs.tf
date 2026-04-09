output "webapp_url" {
  value = "https://${azurerm_linux_web_app.app.default_hostname}"
}

output "postgresql_fqdn" {
  value       = azurerm_postgresql_flexible_server.db.fqdn
  description = "The fully qualified domain name of the PostgreSQL server"
}

output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}