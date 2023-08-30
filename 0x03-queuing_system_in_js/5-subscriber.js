// Import necessary modules
import redis from 'redis';

// Create a Redis subscriber client
const subscriber = redis.createClient();

// Set up event handlers for the subscriber client
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the "holberton school channel"
subscriber.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
subscriber.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
