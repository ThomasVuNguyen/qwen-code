# Supported Model Services

This document outlines the model services supported by this tool.

## Primary Support

### Google Gemini

The tool is built to work with Google's Gemini models through various authentication methods:

*   **Google Account:** For use with Gemini Code Assist.
*   **Gemini API Key:** Obtainable from Google AI Studio.
*   **Vertex AI API Key:** For use with Google Cloud's Vertex AI platform.
*   **Google Cloud Application Default Credentials:** For seamless authentication within the Google Cloud ecosystem.

### OpenAI

The tool also provides first-class support for OpenAI models. You can configure it to use the OpenAI API with your own API key.

*   **Supported Models:** `gpt-4o`, `gpt-4-turbo`, `gpt-4`, `gpt-3.5-turbo`, and other models available through the OpenAI API.
*   **Custom Endpoints:** You can use custom OpenAI-compatible endpoints, which allows for integration with services like Azure OpenAI or local OpenAI-compatible servers.

## Other Services

### Anthropic (Claude), Mistral, Ollama

The documentation does not explicitly mention direct integration with Anthropic, Mistral, or Ollama.

However, the support for custom OpenAI-compatible endpoints opens up the possibility of using a service that provides an OpenAI-compatible interface for these models. This would be an advanced use case and is not officially supported out-of-the-box.
