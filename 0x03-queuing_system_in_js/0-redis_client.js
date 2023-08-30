// Import necessary modules
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Set up event handlers for the Redis client
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Gracefully handle Ctrl+C (SIGINT) to close the Redis connection
process.on('SIGINT', () => {
  client.quit(() => {
    console.log('Redis client disconnected from the server');
    process.exit(0);
  });
});
